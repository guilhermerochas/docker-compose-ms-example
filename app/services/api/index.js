const Express = require('express');
const app = Express();

const products =
  [
    {
      "product": "smartphone"
    },
    {
      "product": "fridge"
    },
    {
      "product": "pen"
    },
    {
      "product": "car"
    },
    {
      "product": "motorcycle"
    },
    {
      "product": "microwave"
    }
  ]



app.get("/", (req, res) => {
  res.json(products);
});

app.listen("3000", () => {
  console.log("express running")
});
