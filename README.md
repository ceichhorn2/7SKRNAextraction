# 7SKRNAextraction
#Purpose of the script:

The script is used to extract the nucleotide sequence of 7SK RNA on chromosome 6 from the genome and renumbering the genomic nucleotide number to start from nucleotide 1 of 7SK RNA till the 3’-end of the sequence.

#Example:

- Locate example input "input.bedgraph" (extracted, piled up coverage and shifted one nucleotide toward the 5'-end) in the repository.
- Run the python script for the input file and compare to the output file (output.bedgraph).

#Description of the output:

Column 1: the number of the 7SK RNA nucleotides
Column 2: the Chromosome number
Column 3: the start nucleotide
Column 4: the end nucleotide
Column 5: the number of cross-linking 
