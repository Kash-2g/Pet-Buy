import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';



// Array of breed objects with names, specialties, and image URLs


function Breeds() {
  const [list,setList] = useState([]);
  useEffect(()=>{
    fetch("http://127.0.0.1:5500/api/breeds")
     .then(response => response.json())
     .then(data => setList(data))
     .catch(error => console.error('Error fetching breeds:', error));
  },[])
  
  const [search, setSearch] = useState('');
  const [filteredList, setFilteredList] = useState([]);

  const handleSearch = (e) => {
    setSearch(e.target.value);
  };

  useEffect(() => {
    const filterList = () => {
      const keywords = search.toLowerCase().split(" ");
      const filteredList = list.filter((breed) => {
        return keywords.every((keyword) => {
          return (
            breed.name.toLowerCase().includes(keyword) ||
            breed.speciality.toLowerCase().includes(keyword)
          );
        });
      });
      setFilteredList(filteredList);
    };

    const delaySearch = setTimeout(() => {
      filterList();
    }, 300);

    return () => clearTimeout(delaySearch);
  }, [search, list]);

  return (
    <div>
      <Navbar />
      <div className="container m-3 p-3">
        <div className="m-2 p-3">
          <input
            onChange={handleSearch}
            className="form-control"
            type="text"
            placeholder="Search breed"
            value={search}
          />
        </div>
        <div className="row">
          {filteredList.map((breed) => (
            <div key={breed.id} className="col-sm-4 mb-3 mx-auto">
              <div className="card">
                <img
                  src={breed.image}
                  className="card-img-top"
                  alt="breed"
                  style={{ height: "350px", width: "350px", objectFit: "cover" }}
                />
                <div className="card-body">
                  <h5 className="card-title">Name: {breed.name}</h5>
                  <p className="card-text">Speciality: {breed.speciality}</p>

                

                 
                </div>
                
                  
               
             
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
  
  

export default Breeds;