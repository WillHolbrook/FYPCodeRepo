import React, {useState, useEffect} from "react";

const Numbers = () => {
  const [numbers, setNumbers] = useState(['one', 'two', 'three'])
  const [letters, setLetters] = useState(['a', 'b', 'c'])

  const addNumber = () => {
    setNumbers([...numbers, 'four'])
  }

  const addLetter = () => {
    setLetters([...letters, 'd'])
  }

  useEffect( () => {
    console.log('Our use effect triggers only on numbers')
  }, [numbers])

  return (
    <React.Fragment>
      <h1>Numbers</h1>
      {numbers.map( num => {
        return (<h4>{num}</h4>)
      })}
      <button onClick={addNumber}>Add Number</button>
      <h1>Letters</h1>
      {letters.map( letter => {
        return (<h4>{letter}</h4>)
      })}
      <button onClick={addLetter}>Add Letter</button>
    </React.Fragment>
  )
}

export default Numbers