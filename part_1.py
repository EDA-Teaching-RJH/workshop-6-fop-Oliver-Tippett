sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
new_findings = []
for i in range(len(sample_bay)):
    print("Transmitting data for: [Sample Name]")
    print (sample_bay)
    break
print (sample_bay[0])
print(sample_bay[len(sample_bay)-1])
print(len(sample_bay))

for i in range(3):
    user_input = input("Enter a rock: ")
    new_findings.append(user_input)

print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    print (sample_bay)