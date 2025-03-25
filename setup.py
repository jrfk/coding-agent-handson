"""
画像モザイク処理ツールのセットアップスクリプト
"""
from setuptools import setup, find_packages

setup(
    name="mosaic-tool",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "pillow>=8.0.0",
        "opencv-python>=4.5.0",
        "dlib>=19.20.0",
    ],
    entry_points={
        "console_scripts": [
            "mosaic-tool=src.mosaic_tool:cli",
        ],
    },
    python_requires=">=3.7",
    author="",
    author_email="",
    description="画像にモザイク処理を適用するCLIツール",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
