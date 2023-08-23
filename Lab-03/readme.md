# Protein Sequence Alignment Using Substitution Matrices

This Python script allows you to align two protein sequences using a substitution matrix as the scoring scheme. It uses the Biopython library for sequence alignment and provides options for choosing a substitution matrix, gap opening penalty, and gap extension penalty.

## Requirements

- Python 3.x
- Biopython library

You can install the required dependencies using the following command:

```bash
pip install biopython
```

## Usage

1. Clone this repository or download the `substitution_matrix_scheme.py` script.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the `substitution_matrix_scheme.py` script.

4. Run the script using the following command:

```bash
python substitution_matrix_scheme.py
```

5. Follow the prompts to input the protein sequences, substitution matrix name (e.g., blosum62 or pam250), gap opening penalty, and gap extension penalty.

6. The script will provide the aligned sequences and the alignment score.

## Example

Here's an example of how the script works:

```
Enter the first protein sequence: MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLYYANKYNGVFQECCQAEDKGACLLPKIETMREKVLASSARQRLRCASIQKFGERALKAWSVARLSQKFPKAEFVEVTKLVTDLTKVHKECCHGDLLECADDRADLAKYICDNQDTISSKLKECCDKPLLEKSHCIAEVEKDAIPENLPPLTADFAEDKDVCKNYQEAKDAFLGSFLYEYSRRHPEYAVSVLLRLAKEYEATLEECCAKDDPHACYSTVFDKLKHLVDEPQNLIKQNCDQFEKLGEYGFQNALIVRYTRKVPQVSTPTLVEVSRSLGKVGTRCCTKPESERMPCTEDYLSLILNRLCVLHEKTPVSEKVTKCCTESLVNRRPCFSALTPDETYVPKAFDEKLFTFHADICTLPDTEKQIKKQTALVELLKHKPKATEEQLKTVMENFVAFVDKCCAADDKEACFAVEGPKLVVSTQTALA
Enter the second protein sequence: MELSFVNLDPALEELDETYVPKAFDEKLFTFHADICTLPDTEKQIKKQTALVELLKHKPKATEEQLKTVMENFVAFVDKCCAADDKEACFAVEGPKLVVSTQTALA
Enter the substitution matrix name (e.g., blosum62): pam250
Enter the gap opening penalty: -12
Enter the gap extension penalty: -1
Aligned Sequence 1: MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLYYANKYNGVFQECCQAEDKGACLLPKIETMREKVLASSARQRLRCASIQKFGERALKAWSVARLSQKFPKAEFVEVTKLVTDLTKVHKECCHGDLLECADDRADLAKYICDNQDTISSKLKECCDKPLLEKSHCIAEVEKDAIPENLPPLTADFAEDKDVCKNYQEAKDAFLGSFLYEYSRRHPEYAVSVLLRLAKEYEATLEECCAKDDPHACYSTVFDKLKHLVDEPQNLIKQNCDQFEKLGEYGFQNALIVRYTRKVPQVSTPTLVEVSRSLGKVGTRCCTKPESERMPCTEDYLSLILNRLCVLHEKTPVSEKVTKCCTESLVNRRPCFSALTPDETYVPKAFDEKLFTFHADICTLPDTEKQIKKQTALVELLKHKPKATEEQLKTVMENFVAFVDKCCAADDKEACFAVEGPKLVVSTQTALA
Aligned Sequence 2: ME-LSFVNL---------------------------------------------------------------------------------------------------------------------------DPALEEL------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------DETYVPKAFDEKLFTFHADICTLPDTEKQIKKQTALVELLKHKPKATEEQLKTVMENFVAFVDKCCAADDKEACFAVEGPKLVVSTQTALA
Alignment Score: -46.0
```

## Customization

You can customize the script by modifying the gap penalties, adding more substitution matrices, or extending its functionality as needed.

Feel free to reach out if you have any questions or suggestions!

```

Remember to adjust the instructions and information as needed. This README provides a basic outline of what the script does, how to use it, and how to customize it.
