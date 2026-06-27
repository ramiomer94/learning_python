cities = ['tokyo', 'salalah', 'socotra', 'maldives', 'patagonia'];
print("Here is the original list:")
print(cities);

print("\nHere is the list sorted alphabetically:");
print(sorted(cities));

print("\nHere is the original list again:")
print(cities);

print("\nHere is the list sorted in the reverse alphabetical order: ");
print(sorted(cities, reverse=True));

print("\nHere is the original list again:")
print(cities);

print("\nHere is the list in the reverse order:");
cities.reverse();
print(cities);

print("\nHere is the list in the original order again:");
cities.reverse();
print(cities);

print("\nHere is the list sorted alphabetically:");
cities.sort();
print(cities);

print("\nHere is the list sorted in reverse alphabetical order:");
cities.sort(reverse=True);
print(cities);