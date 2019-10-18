import React from 'react';
import TodoItem from './TodoItem'
class MainContent extends React.Component{


  render(){
    var listStyle = {
      color: "#e5e285",
      backgroundColor: "#354154"
    }

    const TodoList = this.props.list.map((candidate) => <TodoItem key = {candidate.id} text = {candidate.name} />);
    return (
      <div className = "todoList" style={listStyle} >
        {TodoList}
      </div>
    )
  }

}

export default MainContent;
