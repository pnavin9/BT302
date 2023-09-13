import random

# Function to perform Gibbs sampling for motif discovery
def gibbs_sampler(protein, k, t, N):
    motifs = [protein[i][random.randint(0, len(protein[i])-k):][:k] for i in range(t)]  # Initialize motifs randomly
    best_motifs = motifs  # Initialize the best motifs with the random motifs
    
    for _ in range(N):  # Iterate N times
        i = random.randint(0, t-1)  # Choose a random sequence index
        motifs.pop(i)  # Remove the motif from the chosen sequence
        profile = create_profile(motifs)  # Create a profile from the remaining motifs
        motifs.insert(i, profile_most_probable(protein[i], k, profile))  # Insert the most probable motif based on the profile
        
        if score_motifs(motifs) < score_motifs(best_motifs):  # Check if the current motifs are better than the best motifs
            best_motifs = motifs  # Update the best motifs if the current motifs are better
            
    return best_motifs

# Function to create a profile matrix from a list of motifs
def create_profile(motifs):
    return [[sum(motif[j] == base for motif in motifs) / len(motifs) for base in 'ACDEFGHIKLMNPQRSTVWY'] for j in range(len(motifs[0]))]

# Function to find the most probable k-mer in a sequence based on a profile matrix
def profile_most_probable(protein, k, profile):
    max_prob = -1
    most_probable = protein[:k]
    
    for i in range(len(protein)-k+1):
        pattern = protein[i:i+k]
        prob = 1
        
        for j in range(k):
            prob *= profile[j]['ACDEFGHIKLMNPQRSTVWY'.index(pattern[j])]
        
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    
    return most_probable

# Function to score a set of motifs based on the consensus sequence
def score_motifs(motifs):
    return sum(len(motifs) - max(motif.count(base) for base in 'ACDEFGHIKLMNPQRSTVWY') for motif in zip(*motifs))

# Example usage
protein = [
    "ACGAGATA",
    "GAGAACTA",
    "TAGAGACC",
    "CACTGAGA",
]
k = 4
t = 3
N = 1000
best_motifs = gibbs_sampler(protein, k, t, N)
print(best_motifs)
