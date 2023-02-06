import React, { useEffect, useMemo } from "react";

function PassRequire(props) {
  const requirement_tuples = useMemo(() => {
    const min_pass_len = 8;
    const max_pass_len = 64;
    const correct_pass_len = (pass) => {
      return min_pass_len <= pass.length && pass.length <= max_pass_len;
    };

    const contains_uppercase_char = (pass) => {
      return /[A-Z]/.test(pass);
    };

    const contains_lowercase_char = (pass) => {
      return /[a-z]/.test(pass);
    };

    const contains_number_char = (pass) => {
      return /[0-9]/.test(pass);
    };

    const special_chars = [
      "~",
      "`",
      "!",
      "@",
      "#",
      "$",
      "%",
      "^",
      "&",
      "*",
      "(",
      ")",
      "_",
      "-",
      "+",
      "=",
      "{",
      "[",
      "}",
      "]",
      "|",
      "\\",
      ":",
      ";",
      '"',
      "'",
      "<",
      ",",
      ">",
      ".",
      "?",
      "/",
    ];
    const contains_special_char = (pass) => {
      return special_chars.some((char) => {
        return pass.includes(char);
      });
    };

    return [
      ["Between 8-64 Characters Long", correct_pass_len],
      ["Contains Uppercase Letter", contains_uppercase_char],
      ["Contains Lowercase Letter", contains_lowercase_char],
      ["Contains Number", contains_number_char],
      [
        "Contains Special Character: " + special_chars.join(""),
        contains_special_char,
      ],
    ];
  }, []);

  const bool_to_class = (bool) => {
    return bool ? "check-passed" : "check-failed";
  };

  useEffect(() => {
    let all_passed = true;
    requirement_tuples.forEach((requirement_tuple) => {
      const pass = props.password ? props.password : "";
      console.log(pass);
      if (!requirement_tuple[1](pass)) {
        all_passed = false;
        return false;
      }
    });

    if (all_passed) {
      props.setPasswordValid(true);
    } else {
      props.setPasswordValid(false);
    }
  }, [props, requirement_tuples]);

  return (
    <div className={"pass-require"}>
      <ul>
        {requirement_tuples.map((requirement_tuple) => {
          return (
            <li className={bool_to_class(requirement_tuple[1](props.password))}>
              {requirement_tuple[0]}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default PassRequire;
