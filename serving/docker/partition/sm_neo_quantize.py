#!/usr/bin/env python
#
# Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for
# the specific language governing permissions and limitations under the License.

import sys
import logging
import os
from types import SimpleNamespace
from typing import Final, Optional

from sm_neo_utils import (InputConfiguration, CompilationFatalError,
                          write_error_to_file, get_neo_env_vars,
                          get_neo_compiler_flags)
from utils import extract_python_jar
from quantization_properties_manager import QuantizationPropertiesManager
from quantize import QuantizationService

PYTHON_CACHE_DIR = '/tmp/djlserving/cache'


class NeoQuantizationService():

    def __init__(self):
        self.args: SimpleNamespace = SimpleNamespace()
        self.properties_manager: QuantizationPropertiesManager = None
        self.compiler_flags: dict = None

        env = get_neo_env_vars()
        #self.NEO_COMPILER_OPTIONS: Final[str] = env[0]
        self.INPUT_MODEL_DIRECTORY: Final[str] = env[1]
        self.OUTPUT_MODEL_DIRECTORY: Final[str] = env[2]
        self.COMPILATION_ERROR_FILE: Final[str] = env[3]
        self.COMPILER_CACHE_LOCATION: Final[str] = env[4]


    def update_dataset_cache_location(self):
        logging.info(f"Updating HuggingFace Datasets cache directory to: {self.COMPILER_CACHE_LOCATION}")
        os.environ['HF_DATASETS_CACHE'] = self.COMPILER_CACHE_LOCATION
        os.environ['HF_DATASETS_OFFLINE'] = "1"

    def initialize_partition_args_namespace(self):
        """
        Initialize args, a SimpleNamespace object that is used to instantiate a
        PropertiesManager for partitioning. PropertiesManager expects an
        argparse.Namespace, but we use a SimpleNamespace in its place because it
        is easier to construct.
        """
        self.args.save_mp_checkpoint_path = self.OUTPUT_MODEL_DIRECTORY
        self.args.engine = "MPI"
        # If skip_copy is not enabled, outputted configs are overwritten, and deployment fails.
        self.args.skip_copy = True
        # These attributes reflect the default values of the corresponding attributes
        # in the partition argparser. PropertiesManager expects these attributes to be defined.
        self.args.model_id = None
        self.args.tensor_parallel_degree = None
        self.args.quantize = None


    def construct_properties_manager(self):
        """
        Factory method used to construct a QuantizationPropertiesManager from
        given serving.properties
        """
        self.args.properties_dir = self.INPUT_MODEL_DIRECTORY
        logging.debug(
            "Constructing PropertiesManager from "
            f"serving.properties\nargs:{self.args}\n")
        self.properties_manager = QuantizationPropertiesManager(self.args)


    def run_quantization(self) -> str:
        """
        :return: the output of the partition command captured from stdout
        """
        quantization_service = QuantizationService(self.properties_manager)
        extract_python_jar(PYTHON_CACHE_DIR)
        try:
            return quantization_service.run_quantization()
        except Exception as exc:
            raise CompilationFatalError(
                f"Encountered an error during quantization: {exc}"
            )

    def neo_quantize(self):
        self.update_dataset_cache_location()
        self.initialize_partition_args_namespace()
        self.construct_properties_manager()
        self.run_quantization()


def main():
    logging.basicConfig(stream=sys.stdout,
                        format="%(message)s",
                        level=logging.INFO,
                        force=True)

    try:
        neo_quantization_service = NeoQuantizationService()
        neo_quantization_service.neo_quantize()
    except Exception as exc:
        write_error_to_file(
            exc, neo_quantization_service.COMPILATION_ERROR_FILE)
        raise exc


if __name__ == "__main__":
    main()
