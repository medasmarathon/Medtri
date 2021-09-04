from medtri.medinode import Host, Observation, Condition
from medtri.medinode import RelativeEvent as Event

symptom_x = Event("Symptom X")
symptom_y = Event("Symptom Y")
symptom_z = Event("Symptom Z")

disease_A = Event("Disease A", prevalence=0.10)
disease_A.has_apriori_event(symptom_x, 0.90)
disease_A.has_apriori_event(symptom_y, 0.20)

disease_B = Event("Disease B", prevalence=0.40)
disease_B.has_apriori_event(symptom_x, 0.60)
disease_B.has_apriori_event(symptom_y, 0.70)

disease_C = Event("Disease C", prevalence=0.30)
disease_C.has_apriori_event(symptom_x, 0.40)
disease_C.has_apriori_event(symptom_y, 0.80)

patient = Host("Human", possible_events=[disease_A, disease_B])

symptom_x_observation = Observation(symptom_x, is_present=True)
symptom_y_observation = Observation(symptom_y, is_present=True)
symptom_z_observation = Observation(symptom_z, is_present=True)

patient_condition = patient | symptom_x_observation

print(disease_A.is_outcome_of(symptom_x))
print(disease_A.prevalence_relative_to_observations([symptom_x_observation]))
