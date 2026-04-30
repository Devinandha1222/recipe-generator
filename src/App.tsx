import { useState } from "react";
import { generateRecipe } from "./api";

function App() {
  const [ingredient, setIngredient] = useState("");
  const [recipe, setRecipe] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!ingredient) return;

    setLoading(true);
    setRecipe("");

    try {
      const data = await generateRecipe(ingredient);
      setRecipe(data.recipe);
    } catch (err) {
      setRecipe("Error generating recipe");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🍳 Recipe Generator</h1>

      <input
        type="text"
        placeholder="Enter ingredient (e.g. chicken)"
        value={ingredient}
        onChange={(e) => setIngredient(e.target.value)}
      />

      <button onClick={handleGenerate}>
        {loading ? "Generating..." : "Generate Recipe"}
      </button>

      <div className="output">
        <pre>{recipe}</pre>
      </div>
    </div>
  );
}

export default App;