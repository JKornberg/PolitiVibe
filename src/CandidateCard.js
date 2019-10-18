import React from 'react';
import Dough from './Dough.js';
import Switch from './Switch.js';
class CandidateCard extends React.Component{

  constructor(props){
    super(props);


    this.handleChange = this.handleChange.bind(this);
    this.state = {
        "checked" : false,
        "percentage" : this.getPolarity(this.props.data, "polarity"),
        "doughData" : this.props.data.favor.slice()
    }

    console.log(this.props.data)
  }

  handleChange(event){
    if (event.target.checked){
      this.setState({
        "checked" : true,
        "percentage" : this.getPolarity(this.props.data, "subjectivity"),
        "doughData" : this.props.data.subjectivity
      })
    } else{
      this.setState({
        "checked" : false,
        "percentage" : this.getPolarity(this.props.data, "polarity"),
        "doughData" : this.props.data.favor
      })
    }
    console.log(this.props.data)
  }





  render(){
    return (
      <div className = "card">
        <div className = "card-body">
          <div className = "card-front">
            <div className= "profileWrapper" style={{backgroundImage: `url(${this.props.data.image})`}}></div>
            <h3> {this.props.data.info.name} </h3>
            <div className="progress">
              <div className="progress-bar" role="progressbar" style= {{"width": this.state.percentage + "%"}} aria-valuenow={this.state.percentage} aria-valuemin="0" aria-valuemax="100"></div>
            </div>
          </div>
          <div className = "card-back">
            <div className = "card-back-container">
              <Dough data = {this.state.doughData} checked = {this.state.checked}/>
              <Switch handleChange = {this.handleChange}/>
            </div>
          </div>
        </div>
      </div>

    )
  }

  getPolarity(data, sentiment){
    const res = (((data['topics']['all'][sentiment] + 1) / 2) * 100).toString()

    return res;
  }




}

export default CandidateCard
