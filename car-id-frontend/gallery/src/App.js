import React, { useState, useEffect } from "react";
import Gallery from "./Gallery";
import Spinner from "react-bootstrap/Spinner";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

const BASE_URL = "http://127.0.0.1:5000/";
//const BASE_URL = "http://moonlandingsol.pythonanywhere.com/"

function prep_for_api(string, year = false) {
  if (year) {
    var formatted_string = string
      .split("-")
      .map((item) => item.trim())
      .join("-");
    return formatted_string;
  } else {
    return string.toLowerCase().replace(/ /g, "-");
  }
}

function App() {
  const [listMakes, setListMakes] = useState([]);
  const [listModels, setListModels] = useState([]);
  const [listYears, setListYears] = useState([]);
  const [make, setMake] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [imageList, setimageList] = useState([]);
  const [loading, setloading] = useState(true);

  useEffect(() => {
    // Get Makes
    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        //Defaults to 'Bugatti'
        setMake(data[11]);
        setListMakes(data);
      });
  }, []);
  useEffect(() => {
    // Get Models
    // Hacky solution to call API
    var fetchMake = prep_for_api(make);
    if (fetchMake) {
      fetch(BASE_URL + fetchMake)
        .then((res) => res.json())
        .then((data) => {
          if (make === "Bugatti") {
            //Defaults to "Chiron"
            setModel(data[1]);
          } else {
            setModel(data[0]);
          }
          setListModels(data);
        });
    }
  }, [make]);
  useEffect(() => {
    // Get Years
    var fetchMake = prep_for_api(make);
    var fetchModel = prep_for_api(model);
    if (fetchMake && fetchModel) {
      fetch(BASE_URL + fetchMake + "/" + fetchModel + "/years")
        .then((res) => res.json())
        .then((data) => {
          setYear(data[0]);
          setListYears([...new Set(data)]);
        });
    }
  }, [model]);
  useEffect(() => {
    var fetchMake = prep_for_api(make);
    var fetchModel = prep_for_api(model);
    var fetchYear = prep_for_api(year, true);

    console.log(BASE_URL + fetchMake + "/" + fetchModel + "/" + fetchYear);
    fetch(BASE_URL + fetchMake + "/" + fetchModel + "/" + fetchYear)
      .then((res) => res.json())
      .then((data) => {
        if (fetchModel) {
          var imageUrls = data[fetchModel]["images"];
          console.log(imageUrls);
          if (imageUrls) {
            setimageList(imageUrls);
            setloading(false);
            //window.scrollTo(window.scrollX, window.scrollY +1000);
          }
        }
      });
  }, [year]);
  return (
    <>
      {!loading ? (
        <Gallery
          onChangeMake={(e) => setMake(e.target.value)}
          onChangeModel={(e) => setModel(e.target.value)}
          onChangeYear={(e) => setYear(e.target.value)}
          selectedMake={make}
          selectedModel={model}
          slectedYear={year}
          listMakes={listMakes}
          listModels={listModels}
          listYears={listYears}
          imageList={imageList}
        />
      ) : (
        <Spinner className="big-spinner" animation="border" variant="light" />
      )}
    </>
  );
}

export default App;
