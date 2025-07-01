{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN5D8Yk5+QUtmZ9KaScSiSB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/deepaksingh4190/leetcode-solutions/blob/main/two_sum_txt.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# brute force : we check the every element with number if they both sum gives us value equal target then we retrn the indexes\n",
        "def TwoSums(nums,target):\n",
        "  for i in range(len(nums)):\n",
        "    for j in range(i+1,len(nums)):\n",
        "      if nums[i]+nums[j] == target:\n",
        "        return [i,j]\n",
        "nums = [2, 7, 11, 15]\n",
        "target = 9\n",
        "print(TwoSums(nums, target))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pSXPcI9kIC-l",
        "outputId": "aee9ff3b-942d-4fd9-f0ff-b01fac9c359d"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1]\n"
          ]
        }
      ]
    }
  ]
}