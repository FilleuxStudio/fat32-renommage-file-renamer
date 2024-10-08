# FAT32 File Renaming & Recovery Utility

This Python script automates the renaming of files recovered from a FAT32-formatted USB drive by assigning the correct file extension based on file type. It supports a wide range of file formats, including JPEG, PNG, PDF, Microsoft Office files, SolidWorks files, and more.

## Features
- Automatically detects file types and renames files with missing or incorrect extensions.
- Supports FAT32 file systems, including files commonly found on damaged or recovered drives.
- Especially useful for `.CHK` or `.unknown` files recovered via `fsck` or `TestDisk`.

## Requirements
- Python 3.x
- `file` command (part of most Linux distributions)

## Prerequisites: USB Drive Recovery and Repair

Before running the script, follow these steps to recover and repair data from your USB drive:

### 1. Identify the USB Drive
Use the following command to list all disks and identify your USB drive:

```bash
sudo fdisk -l
```
Note the device name (e.g., `/dev/sdb`).

### 2. Unmount the USB Drive
Before running any repair commands, unmount the USB drive (replace `X` with the partition number, usually `1`):

```bash
sudo umount /dev/sdbX
```

### 3. Perform a Preliminary Check
Run an initial check without making any modifications:

```bash
sudo fsck -n /dev/sdbX
```

### 4. Full Check and Repair
To perform a full check and automatically fix errors, use:

```bash
sudo fsck -t auto -A -V -C -f -y -v /dev/sdbX
```

#### Explanation of options:
- `-t auto`: Automatically detects the file system type.
- `-A`: Checks all file systems listed in `/etc/fstab`.
- `-V`: Verbose mode, provides detailed output.
- `-C`: Displays a progress bar during the check.
- `-f`: Forces the check, even if the file system appears clean.
- `-y`: Automatically answers "yes" to all prompts.
- `-v`: Additional verbose mode for more detailed output.

#### Other useful options:
- `-c`: Checks for bad blocks.
- `-r`: Interactive mode for repairs, allowing user input.
- `-p`: Automatically repairs the file system without asking questions.
- `-n`: Dry run, performs checks without making any modifications.
- `-B`: Searches for bad blocks during the file system check.
- `-l`: Lists file names during the verification process.
- `-a`: Automatically repairs the file system without user interaction.

### 5. Aggressive Repair (if errors persist)
If errors are still present, try a more aggressive repair for FAT file systems:

```bash
sudo fsck.vfat -a -w -v /dev/sdbX
```

### 6. Check for Bad Blocks
To check for physical defects on the USB drive:

```bash
sudo badblocks -sv /dev/sdbX
```

### 7. Data Recovery with TestDisk (if necessary)
If the file system cannot be repaired, attempt recovery using TestDisk:

```bash
sudo testdisk /dev/sdbX
```

### 8. Recover Files with PhotoRec (as a last resort)
For extreme cases, recover individual files using PhotoRec:

```bash
sudo photorec /dev/sdbX
```

### 9. Remount the USB Drive
After repairs, remount the USB drive:

```bash
sudo mount /dev/sdbX /mnt
```

### 10. Check USB Drive Content
Verify the files on the USB drive:

```bash
ls -l /mnt
```

## Running the Script

Once you have repaired your USB drive and recovered the files, navigate to the directory containing the files you wish to rename and run the Python script:

```bash
python3 rename_files.py
```

The script will:
1. Detect file types using the `file` command.
2. Rename files based on their detected types, adding the correct extensions.

### Example Output:
```bash
Renamed file001.CHK to file001.jpg
Skipped file002.unknown (no change needed)
```

## Supported File Types
- Images: JPEG, PNG
- Documents: PDF, Microsoft Word, Excel
- Archives: ZIP, 7-zip
- Executables: `.exe`, `.dll`
- SolidWorks: `.sldprt`, `.sldasm`, `.slddrw`
- Text files: `.txt`
- Data files: `.dat`

You can easily add support for additional file types by modifying the script.