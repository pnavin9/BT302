# Protein Sequence Alignment using Clustal Omega

This repository provides a Python script for performing progressive multiple sequence alignment using the Clustal Omega tool from the Biopython library. Multiple sequence alignment is a fundamental task in bioinformatics that helps identify conserved regions and structural motifs among a set of protein sequences.

## Getting Started

### Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Biopython
- Clustal Omega

You can install Biopython using pip:

```bash
pip install biopython
```

Clustal Omega can be downloaded and installed following the instructions provided on its [official website](http://www.clustal.org/omega/).

### Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/protein-alignment.git
cd lab-04
```

2. Run the script:

```bash
python three_sequence_alignment.py
```

Follow the on-screen prompts to enter protein sequences. You need to input at least three sequences.

3. The aligned sequences will be printed to the console and saved in the `aligned_sequences.fasta` file.

## About the Script

The provided script (`align_sequences.py`) demonstrates how to use Biopython's SeqIO and ClustalOmegaCommandline modules to perform multiple sequence alignment. Here's a breakdown of the script's functionality:

1. **Input**: The script prompts you to enter protein sequences. It expects at least three sequences for meaningful alignment.

2. **Alignment**: The sequences are aligned using Clustal Omega. The alignment process helps identify conserved regions among the input sequences.

3. **Output**: The aligned sequences are printed to the console in FASTA format, showing the sequence names and their corresponding aligned sequences.

4. **Cleanup**: Temporary files are removed once the alignment process is complete.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The script utilizes the Biopython library, which is a valuable resource for bioinformatics tasks.
- Clustal Omega is developed by the European Bioinformatics Institute (EMBL-EBI) and is a widely used tool for multiple sequence alignment.

Feel free to contribute to this repository by reporting issues, suggesting enhancements, or submitting pull requests. Your contributions are greatly appreciated!
