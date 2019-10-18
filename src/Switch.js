import React, {Component} from 'react';
import './switch.css';

class Switch extends Component{

  constructor(props){
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event){
    console.log(event.target.checked);
  }

  render(){
    return(
      <label className = "switch">
        <input type="checkbox" onChange = {(event) => this.props.handleChange(event)} />
        <div className = "slider" />
      </label>
  )}

}

export default Switch;
