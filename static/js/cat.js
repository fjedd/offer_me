const url = "https://api.thecatapi.com/v1/images/search";
const container = document.getElementById("catContainer");
const button = document.getElementById("catButton");

button.addEventListener("click", getCatImage);

catImage = (json) => {
  let photo = json[0].url;
  let image = document.createElement("img");
  image.src = photo;
  image.alt = photo;
  container.appendChild(image);
};

async function getCatImage() {
  container.innerHTML = "";
  try {
    const response = await fetch(url);
    const json = await response.json();
    return catImage(json);
  } catch (e) {
    console.log("Meowerror");
    console.log(e);
  }
}
