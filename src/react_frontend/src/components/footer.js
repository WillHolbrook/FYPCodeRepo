import React, {Component} from "react";
import {MyContext} from "../index";

class Footer extends Component {


  state = {
    name: "",
    age: 21,
    trademark: "by Will"
  }

  componentDidMount() {
    this.setState({name: 'MyName'})
    //Subscribe
  }

  componentWillUnmount() {
    this.setState({name: 'Unmounting'})
    //Unsubscribe
  }

  changed = evt => {
    // console.log('changed', evt.target.value)
    this.setState({name: evt.target.value})
    console.log(this.state)
  }

  render() {

    const animals = ['cat', 'dog', 'elephant']

    return (
      <React.Fragment>
        <h3 onClick={this.props.myalert}>
          {this.state.trademark}
        </h3>
        <input
          value={this.state.name}
          onChange={this.changed} type="text"/>
        {this.state.age >= 18 ? (<h4>yes come buy some alcohol</h4>) : (<h1>no! Get Out!</h1>)}

        <div>
          {animals.map(animal => {
            return (
              <h1 key={animal}>
                {animal}
              </h1>)
          })}
        </div>
        <MyContext.Consumer>
          {({animals}) => (
            animals.map(animal => {
              return (
                <h2 key={animal} style={{color: 'blue'}}>
                  {animal}
                </h2>)
            })
          )}
        </MyContext.Consumer>
      </React.Fragment>
    )
  }
}

export default Footer;