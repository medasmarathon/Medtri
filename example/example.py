from medtri.medinode.event.eventlink import add_event_link
from medtri.medinode.inode.constants import EventRelation as Relation
from medtri.medinode import Host, Observation, Condition
from medtri.medinode import RelativeEvent as Event

symptom_x = Event("Symptom X")
symptom_y = Event("Symptom Y")
symptom_z = Event("Symptom Z")
symptom_x_y_compound = Event("Symptom X Y")
symptom_x_y_compound.observations = [Observation(symptom_x, True), Observation(symptom_y, True)]

disease_A = Event("Disease A", prevalence=0.10)

disease_B = Event("Disease B", prevalence=0.40)

disease_C = Event("Disease C", prevalence=0.30)

patient = Host("Human", possible_events=[disease_A, disease_B, disease_C])
add_event_link(Relation.APRIORI, symptom_x, disease_A, 0.9)
add_event_link(Relation.APRIORI, symptom_y, disease_A, 0.2)
add_event_link(Relation.APRIORI, symptom_x, disease_B, 0.6)
add_event_link(Relation.APRIORI, symptom_y, disease_B, 0.7)
add_event_link(Relation.APRIORI, symptom_x, disease_C, 0.4)
add_event_link(Relation.APRIORI, symptom_y, disease_C, 0.8)

symptom_x_observation = Observation(symptom_x, is_present=True)
symptom_y_observation = Observation(symptom_y, is_present=True)
symptom_z_observation = Observation(symptom_z, is_present=True)

patient_condition = patient | [symptom_x_observation]

print(patient.is_event_possible(symptom_y))
print(disease_A.prevalence_relative_to_observations([symptom_x_observation]))
print(patient_condition.probability_of(disease_A))
