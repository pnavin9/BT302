# Gibbs Sampler for Motif Discovery

## Overview

This Python script implements the Gibbs sampling algorithm for motif discovery in a set of DNA or protein sequences. Gibbs sampling is a probabilistic algorithm used to find motifs, which are short, recurring sequences in a set of input sequences. The goal is to identify motifs that are statistically significant and likely to be binding sites for transcription factors or other regulatory elements.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system (Python 3 recommended).

2. Download the `gibbs_sampler.py` script.

3. Prepare your input data:
   - Define your protein sequences as a list of strings, where each string represents a sequence.
   - Set the values of `k` (motif length), `t` (number of sequences), and `N` (number of Gibbs sampling iterations) in the script.

4. Run the script using a Python interpreter:


5. The script will perform Gibbs sampling and output the best motifs discovered in the input sequences.

## Functions

The script contains the following functions:

- `gibbs_sampler(protein, k, t, N)`: Performs Gibbs sampling to discover motifs in a set of protein sequences.
- `create_profile(motifs)`: Creates a profile matrix from a list of motifs.
- `profile_most_probable(protein, k, profile)`: Finds the most probable k-mer in a sequence based on a profile matrix.
- `score_motifs(motifs)`: Scores a set of motifs based on the consensus sequence.

## Example

An example usage of the script is provided with sample protein sequences. You can uncomment the example usage section in the script to run it and observe the results.

## Dependencies

The script does not have external dependencies and relies on Python's built-in libraries.

## License

This script is provided under the MIT License. You are free to use and modify it as needed. Refer to the LICENSE file for more details.

## Author

Navin Patwari
p.navin@iitg.ac.in
