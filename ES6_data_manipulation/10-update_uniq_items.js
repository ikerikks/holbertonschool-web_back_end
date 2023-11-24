export default function updateUniqueItems(map) {
  map.forEach((value, key) => {
    value === 1 ? map.set(key, 100): value;
  });

  return map;
}
