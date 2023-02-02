import React, {useEffect} from "react";

function PassRequire(props) {

  const min_pass_len = 8
  const max_pass_len = 64
  const correct_pass_len = () => {
    return min_pass_len <= props.password.length && props.password.length <= max_pass_len
  }

  const contains_uppercase_char = () => {
    return /[A-Z]/.test(props.password)
  }

  const contains_lowercase_char = () => {
    return /[a-z]/.test(props.password)
  }

  const contains_number_char = () => {
    return /[0-9]/.test(props.password)
  }

  const special_chars = ['\~','\`','\!','\@','\#','\$','\%','\^','\&','\*','\(','\)','\_','\-','\+','\=','\{','\[','\}','\]','\|','\\','\:','\;','\"','\'','\<','\,','\>','\.','\?','\/']
  const contains_special_char = () => {
    return special_chars.some(char => {return props.password.includes(char)})
  }

  const bool_to_class = bool => {
    return bool ? "check-passed" : "check-failed"
  }

  const requirement_tuples = [
    ["Between 8-64 Characters Long", correct_pass_len],
    ["Contains Uppercase Letter", contains_uppercase_char],
    ["Contains Lowercase Letter", contains_lowercase_char],
    ["Contains Number", contains_number_char],
    ["Contains Special Character: " + special_chars.join(""), contains_special_char],
  ]

  useEffect(() => {
    let all_passed = true
    requirement_tuples.map(requirement_tuple => {
      if (!requirement_tuple[1]()) {
        all_passed = false
      }
    })

    if (all_passed) {
      props.setPasswordValid(true)
    }
    else {
      props.setPasswordValid(false)
    }
  }, [props.password])


  return (<div className={"pass-require"}>
    <ul>
      {requirement_tuples.map(requirement_tuple => {
        return <li className={bool_to_class(requirement_tuple[1]())}>{requirement_tuple[0]}</li>
      })}
    </ul>
  </div>)
}

export default PassRequire