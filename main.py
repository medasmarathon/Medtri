from medtri.medinode import Event

symptom_x = Event("Symptom X")
symptom_y = Event("Symptom Y")
symptom_z = Event("Symptom Z")

disease_A = Event("Disease A", prevalence=10)
disease_A.has_apriori_factor(symptom_x, 90)
disease_A.has_apriori_factor(symptom_y, 20)

disease_B = Event("Disease A", prevalence=40)
disease_B.has_apriori_factor(symptom_x, 60)
disease_B.has_apriori_factor(symptom_y, 70)

disease_C = Event("Disease A", prevalence=30)
disease_C.has_apriori_factor(symptom_x, 40)
disease_C.has_apriori_factor(symptom_y, 80)
