import React from 'react';
import CandidateCard from './CandidateCard';
import MainContent from './MainContent';
import Navbar from './Navbar';
import candidate_data from './candidate_data';
import Chart from './Chart';
import sentimentData from './data/sentimentData';


class App extends React.Component{



  constructor(props){
    super(props);

    this.state = {
    }
  }

  render(){
    const candidates = sentimentData.map(function (candidate){
      return <CandidateCard key = {candidate.info.name} data={candidate} />
    })

    return (
      <div>
        <Navbar />
        <div className = "container">
          <div className = "row card-holder">
            {candidates}
          </div>
        </div>
        <Chart data = {sentimentData}/>
      </div>
    )
  }

}

export default App;
