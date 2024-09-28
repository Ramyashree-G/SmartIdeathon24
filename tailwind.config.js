module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
   daisyui: {
    themes: [
    {
        cache: {

"primary": "#fcc55e",

"secondary": "#0f766e",

"accent": "#22d3ee",

"neutral": "#fbcfe8",

"base-100": "#ffffff",

"info": "#38bdf8",

"success": "#4ade80",

"warning": "#f97316",

"error": "#dc2626",
          },
        },
      "light",
      "dark",
      "cupcake",
      "bumblebee",
      "emerald",
      "corporate",
      "synthwave",
      "retro",
      "cyberpunk",
      "valentine",
      "halloween",
      "garden",
      "forest",
      "aqua",
      "lofi",
      "pastel",
      "fantasy",
      "wireframe",
      "black",
      "luxury",
      "dracula",
      "cmyk",
      "autumn",
      "business",
      "acid",
      "lemonade",
      "night",
      "coffee",
      "winter",
      "dim",
      "nord",
      "sunset",
    ],
  },
}
