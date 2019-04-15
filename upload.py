#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# Minio client dependencies
from minio import Minio
from minio.policy import Policy

S3_BUCKET = os.environ.get("S3_BUCKET", "bucket")
S3_HOST = os.environ.get("S3_HOST", "play.minio.io")
S3_KEY = os.environ.get("S3_KEY", "Q3AM3UQ867SPQQA43P2F")
S3_SECRET = os.environ.get("S3_SECRET", "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG")

# TODO: Rewrite upload script with Minio
# TODO: Find a way to read Drone env