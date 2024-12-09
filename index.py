from pathlib import Path

path = "C:/Users/Zbook/Desktop"

downloads = Path.home() / "Downloads"
document_path = downloads / "Documents"
compressed_path = downloads / "Compressed"

document = {
    ".txt",
    ".doc",
    ".docx",
    ".pdf",
    ".odt",
    ".rtf",
    ".tex",
    ".md",
    ".xls",
    ".xlsx",
    ".ods",
    ".csv",
    ".tsv",
    ".ppt",
    ".pptx",
    ".key",
    ".epub",
    ".pages",
}
compressed = {
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".bz2",
    ".xz",
    ".tar.gz",
    ".tar.bz2",
    ".tar.xz",
}

for item in downloads.iterdir():
    if item.is_file() and item.suffix in document:
        item.rename(document_path / item.name)
    elif item.is_file() and item.suffix in compressed:
        item.rename(compressed_path / item.name)
