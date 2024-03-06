import matplotlib.pyplot as plt
import json

def read_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data["activity_weights"]

# Read data
princeton = read_data("./2023-12-06_submissions/Princeton_University_2023-11-29_18-33-21.json")
reading = read_data("./2023-12-06_submissions/University_of_Reading_2023-12-11_10-18-14.json")
heidelberg = read_data("./2023-12-06_submissions/Scientific_Software_Center_2023-12-21_13-13-27.json")
jena = read_data("./2023-12-06_submissions/Friedrich_Schiller_University_Jena_2023-12-06_10-43-44.json")

activities = [
        "RSE Network",
        "Partner Network",
        "RSE Teaching",
        "RSE Consultation",
        "SW Development",
        "SW Maintenance",
        "RSE Infrastructure",
        "RSE Research",
        "RSE Outreach"
    ]
colors = plt.cm.Paired(range(len(activities)))

# Mapping activities to colors
activity_to_color = {activity: colors[i] for i, activity in enumerate(activities)}

# Creating the joint plot
fig, axs = plt.subplots(2, 2, figsize=(16, 16))

# Plot for Jena
axs[0, 0].pie(jena, colors=colors, startangle=140)
axs[0, 0].set_title('Kompetenzzentrum Digitale Forschung\n Friedrich Schiller University Jena', fontsize=20)

# Plot for Heidelberg
axs[0, 1].pie(heidelberg, colors=colors, startangle=140)
axs[0, 1].set_title('Scientific Software Center\n Heidelberg University', fontsize=20)

# Plot for Princeton
axs[1, 1].pie(princeton, colors=colors, startangle=140)
axs[1, 1].set_title('Research Software Engineering Group\n Princeton University', fontsize=20)

# Plot for Reading
axs[1, 0].pie(reading, colors=colors, startangle=140)
axs[1, 0].set_title('Research Software Engineering\n The University of Reading', fontsize=20)

# Shared legend
fig.legend(activities, title="Activities", loc="center right", bbox_to_anchor=(1.1, 0.5), fontsize=20)


fig.savefig("group_composition_plot.pdf", bbox_inches='tight')
# # Adjust layout
# plt.tight_layout()
# plt.show()
