const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function generateRecipe(ingredient: string) {
  const query = new URLSearchParams({ ingredient: ingredient.trim() });
  const res = await fetch(`${BASE_URL}/generate?${query.toString()}`);

  if (!res.ok) {
    throw new Error("Failed to fetch recipe");
  }

  return res.json();
}