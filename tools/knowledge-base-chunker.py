"""
Knowledge Base Chunker
-----------------------
Splits large documents into LLM-friendly chunks with overlap.

When feeding documents to an AI agent, oversized docs cause context overflow
or poor retrieval. This tool chunks them correctly for upload.

Usage:
    python knowledge-base-chunker.py --file your_document.txt
    python knowledge-base-chunker.py --file your_document.txt --chunk-size 500 --overlap 50

Output:
    Numbered .txt chunk files in a /chunks/ subfolder, ready to upload.

No dependencies. Pure Python stdlib.
"""

import argparse
import re
import sys
from pathlib import Path


DEFAULT_CHUNK_SIZE = 800  # words per chunk
DEFAULT_OVERLAP = 80      # words of overlap between chunks


def clean_text(text):
    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def split_into_chunks(text, chunk_size=DEFAULT_CHUNK_SIZE, overlap=DEFAULT_OVERLAP):
    words = text.split()
    total_words = len(words)
    chunks = []
    start = 0
    index = 1

    while start < total_words:
        end = min(start + chunk_size, total_words)
        chunk_words = words[start:end]

        chunks.append({
            "index": index,
            "text": " ".join(chunk_words),
            "word_count": len(chunk_words),
            "start_word": start,
            "end_word": end,
        })

        start += chunk_size - overlap
        index += 1

        if end == total_words:
            break

    return chunks


def chunk_file(file_path, chunk_size=DEFAULT_CHUNK_SIZE, overlap=DEFAULT_OVERLAP, output_dir=None):
    input_path = Path(file_path)
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    text = clean_text(input_path.read_text(encoding="utf-8"))
    chunks = split_into_chunks(text, chunk_size=chunk_size, overlap=overlap)

    out_path = Path(output_dir) if output_dir else input_path.parent / "chunks"
    out_path.mkdir(parents=True, exist_ok=True)

    written = []
    for chunk in chunks:
        chunk_file = out_path / f"{input_path.stem}_chunk_{chunk['index']:03d}.txt"
        header = (
            f"[Document: {input_path.name}] "
            f"[Chunk {chunk['index']} of {len(chunks)}] "
            f"[Words {chunk['start_word']}–{chunk['end_word']}]\n\n"
        )
        chunk_file.write_text(header + chunk["text"], encoding="utf-8")
        written.append(chunk_file)

    return written, chunks


def main():
    parser = argparse.ArgumentParser(description="Split a document into LLM-friendly chunks.")
    parser.add_argument("--file", required=True, help="Path to input .txt or .md file")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE)
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP)
    parser.add_argument("--output-dir", default=None)

    args = parser.parse_args()

    try:
        written, chunks = chunk_file(args.file, args.chunk_size, args.overlap, args.output_dir)
        out_dir = args.output_dir or str(Path(args.file).parent / "chunks")
        total_words = sum(c["word_count"] for c in chunks)

        print(f"\nChunked successfully")
        print(f"  Total words:  {total_words:,}")
        print(f"  Chunks:       {len(chunks)}")
        print(f"  Output dir:   {out_dir}")
        print(f"\nUpload chunk files to CloudyBot (cloudybot.ai) or your vector store.")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
