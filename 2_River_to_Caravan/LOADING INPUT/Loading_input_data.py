{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43cc54ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading dataset...\n",
      "Failed to download file. HTTP Status Code: 404\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "import zipfile\n",
    "from io import BytesIO\n",
    "\n",
    "# Constants\n",
    "ZENODO_DOI = \"10.5281/zenodo.15518099\"\n",
    "DATA_FOLDER = \"data\"\n",
    "DOWNLOAD_URL = \"https://zenodo.org/record/15518099/files/zenodo_data.zip?download=1\"  # Replace if the filename is different\n",
    "\n",
    "# Step 1: Create data directory if it doesn't exist\n",
    "os.makedirs(DATA_FOLDER, exist_ok=True)\n",
    "\n",
    "# Step 2: Download the ZIP file\n",
    "print(\"Downloading dataset...\")\n",
    "response = requests.get(DOWNLOAD_URL)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    print(\"Download successful. Extracting files...\")\n",
    "    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:\n",
    "        zip_ref.extractall(DATA_FOLDER)\n",
    "    print(f\"Files extracted to ./{DATA_FOLDER}\")\n",
    "else:\n",
    "    print(f\"Failed to download file. HTTP Status Code: {response.status_code}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
