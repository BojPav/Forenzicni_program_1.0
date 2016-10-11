print "Welcome to Forenzicni program 1.0" + "\n"

hair_color_black = "CCAGCAATCGC"
hair_color_brown = "GCCAGTGCCG"
hair_color_blonde = "TTAGCTATCGC"

facial_shape_square = "GCCACGG"
facial_shape_round = "ACCACAA"
facial_shape_oval = "AGGCCTCA"

eye_color_blue = "TTGTGGTGGC"
eye_color_green = "GGGAGGTGGC"
eye_color_brown = "AAGTAGTGAC"

gender_female = "TGAAGGACCTTC"
gender_male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

eva_dna = [gender_female, race_white, hair_color_blonde, eye_color_blue, facial_shape_oval]

larisa_dna = [gender_female, race_white, hair_color_brown, eye_color_brown, facial_shape_oval]

matej_dna = [gender_male, race_white, hair_color_black, eye_color_blue, facial_shape_oval]

miha_dna = [gender_male, race_white, hair_color_brown, eye_color_green, facial_shape_square]


dna_file = open("dna.txt").read()

print "Searching DNA..."
print "Comparing suspected DNA..." + "\n"


if gender_male and race_white and hair_color_brown and eye_color_green and facial_shape_square in dna_file:
    print "Miha je pojedel sladoled !"
elif gender_female and race_white and hair_color_brown and eye_color_brown and facial_shape_oval in dna_file:
    print "Larisa je pojedla sladoled !"
elif gender_male and race_white and hair_color_black and eye_color_blue and facial_shape_oval in dna_file:
    print "Matej je pojedel sladoled !"
elif gender_female and race_white and hair_color_blonde and eye_color_blue and facial_shape_oval in dna_file:
    print "Eva je pojedla sladoled !"
else:
    print "Nihce od osumljencev ni storil zlocina..."

print "END!"