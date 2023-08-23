from Bio import pairwise2
from Bio.Align import substitution_matrices

def get_substitution_matrix(substitution_matrix_name):
    substitution_matrix_name = substitution_matrix_name.upper()
    matrices = {
        substitution_matrix_name : substitution_matrices.load(substitution_matrix_name),
        #"pam250": substitution_matrices.load("PAM250"),
        # Add more matrices if needed
    }
    return matrices.get(substitution_matrix_name, None)

def align_sequences(seq1, seq2, substitution_matrix_name, gap_open, gap_extend):
    substitution_matrix = get_substitution_matrix(substitution_matrix_name)
    if substitution_matrix is None:
        raise ValueError("Substitution matrix not found")

    alignments = pairwise2.align.globalds(
        seq1, seq2, substitution_matrix, gap_open, gap_extend
    )

    best_alignment = alignments[0]
    aligned_seq1 = best_alignment[0]
    aligned_seq2 = best_alignment[1]
    alignment_score = best_alignment[2]

    return aligned_seq1, aligned_seq2, alignment_score

if __name__ == "__main__":
    seq1 = input("Enter the first protein sequence: ")
    seq2 = input("Enter the second protein sequence: ")
    matrix_name = input("Enter the substitution matrix name (e.g., blosum62): ")
    gap_open = float(input("Enter the gap opening penalty: "))
    gap_extend = float(input("Enter the gap extension penalty: "))

    aligned_seq1, aligned_seq2, alignment_score = align_sequences(
        seq1, seq2, matrix_name, gap_open, gap_extend
    )

    print("Aligned Sequence 1:", aligned_seq1)
    print("Aligned Sequence 2:", aligned_seq2)
    print("Alignment Score:", alignment_score)
