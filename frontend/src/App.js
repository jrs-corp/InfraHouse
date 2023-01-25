import logo from './logo.svg';
import {useState} from 'react'
import './App.css';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
// import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import axios from 'axios'
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

import '@fontsource/roboto/300.css';


function App() {

  // const [age, setAge] = React.useState('');
  const [message, setMessage] = useState('');
  const [inputmessage, setInputMessage] = useState('');
  const [updated, setUpdated] = useState(message);

  // Radio Value
  const [radiovalue, setRadioValue] = useState('code');

  const handleRadioChange = (event) => {
    console.log(event.target.value)
    setRadioValue(event.target.value);
  };

  const handleChange = (event) => {
    setMessage(event.target.value)
  }

  const handleListChange = (event) => {
    console.log('---')
    console.log(event.target.value)
    setInputMessage(event.target.value)
  }

  const toggleButtonState = (event) => {
    console.log('Running')
    console.log(message)
    console.log(inputmessage)
    console.log(radiovalue)
    // axios.get('http://34.224.40.128:5000/')
    // .then(
    //   (response) => {
    //     console.log(response.data)
    //     // setUpdated(response.data)
    //   }
    // )
    axios.post('/toutes', 
    {
        "platform": inputmessage,
        "codelocation": message
    }
    )
    .then(  
      (response) => {
        console.log(response.data)
      }
    )
  }

  // const handleChange = (event: SelectChangeEvent) => {
  //   // setAge(event.target.value);
  // };

  // toggleButtonState = () => {
  //   console.log('Button is Clicked')
  // }
  

  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <img src={logo} className="App-logo" alt="logo" /> */}

        <br />
    
    <Typography variant="h1" gutterBottom>
        InfraHouse
      </Typography>
        <br />

        <FormControl sx={{ m: 1, minWidth: 80 }}>
        <InputLabel id="demo-simple-select-autowidth-label">Cloud</InputLabel>
        <Select
          labelId="demo-simple-select-autowidth-label"
          id="demo-simple-select-autowidth"
          // value={age}
          onChange={handleListChange}
          autoWidth
          label="Cloud"
        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          <MenuItem value={'AWS'}>AWS</MenuItem>
          <MenuItem value={'GCP'}>GCP</MenuItem>
          <MenuItem value={'Azure'}>Azure</MenuItem>
        </Select>
      </FormControl>





{/* Radio Here */}
      
<RadioGroup
              aria-labelledby="demo-controlled-radio-buttons-group"
              name="controlled-radio-buttons-group"
              value={radiovalue}
              onChange={handleRadioChange}
            >
              <FormControlLabel value="code" control={<Radio />} label="Dockerized Code(Vanilla)" />
              <FormControlLabel value="image" control={<Radio />} label="Docker Image" />
            </RadioGroup>

            {/* Radio here */}















    <br />
        {/* <Typography variant="button" display="block" gutterBottom>
        File Location
      </Typography> */}
      <TextField 
        id="outlined-basic" 
        label="File Location" 
        variant="outlined" 
        // value={message}
        onChange={handleChange}
      />







        <br />
        <br />
        <Button onClick={toggleButtonState} variant="contained">Deploy</Button>

        
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      {/* </header> */}
    </div>
  );
}

export default App;
