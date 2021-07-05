//TinEYE
let TinEye = require('tineye-api')


let privateKey= '6mm60lsCNIB,FwOWjJqA80QZHh9BMwc-ber4u=t^'
let publicKey = 'LCkn,2K7osVwkX95K4Oy'

let api = new TinEye('https://api.tineye.com/rest/', publicKey, privateKey);
let str = "Further Details : \n";

let url = "https://tineye.com/images/meloncat.jpg";


let options = {
  limit: 5,
  sort: "score",
  order: "desc",
};

api
  .searchUrl(url, options)
  .then(function (response) {
    console.log(response);
    console.log(str);
    console.log(response.results);
  })
  .catch(function (error) {
    console.log(error);
  });

// GOOGLE Reverse Image Search

const SerpApi = require('google-search-results-nodejs');
const search = new SerpApi.GoogleSearch("secret_api_key"); //API KEY

const params = {
  engine: "google_reverse_image",
  image_url: "https://i.imgur.com/5bGzZi7.jpg"
};

const callback = function(data) {
  console.log(data['inline_images']);
};

// Show result as JSON
search.json(params, callback);
