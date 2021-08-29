from medtri.medinode import BaseEvent, Host, Observation, Condition

symptom_x = BaseEvent("Symptom X")
symptom_y = BaseEvent("Symptom Y")
symptom_z = BaseEvent("Symptom Z")

disease_A = BaseEvent("Disease A", prevalence=10)
disease_A.has_apriori_event(symptom_x, 90)
disease_A.has_apriori_event(symptom_y, 20)

disease_B = BaseEvent("Disease B", prevalence=40)
disease_B.has_apriori_event(symptom_x, 60)
disease_B.has_apriori_event(symptom_y, 70)

disease_C = BaseEvent("Disease C", prevalence=30)
disease_C.has_apriori_event(symptom_x, 40)
disease_C.has_apriori_event(symptom_y, 80)

patient = Host("Human", possible_events=[disease_A, disease_B, disease_C])

symptom_x_observation = Observation(symptom_x, is_observed=True, is_present=True)
symptom_y_observation = Observation(symptom_y, is_observed=True, is_present=True)
symptom_z_observation = Observation(symptom_z, is_observed=True, is_present=True)

patient_condition = Condition(patient, [symptom_x_observation])

print(disease_A.is_outcome_of(symptom_x))
