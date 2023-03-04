import React, { useEffect, useMemo } from "react";

function PassRequire(props) {
  const requirementTuples = useMemo(() => {
    const minPassLen = 8;
    const maxPassLen = 64;
    const correctPassLen = (pass) => {
      return minPassLen <= pass.length && pass.length <= maxPassLen;
    };

    const containsUppercaseChar = (pass) => {
      return /[A-Z]/.test(pass);
    };

    const containsLowercaseChar = (pass) => {
      return /[a-z]/.test(pass);
    };

    const containsNumberChar = (pass) => {
      return /[0-9]/.test(pass);
    };

    const specialChars = [
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
    const containsSpecialChar = (pass) => {
      return specialChars.some((char) => {
        return pass.includes(char);
      });
    };

    return [
      ["Between 8-64 Characters Long", correctPassLen],
      ["Contains Uppercase Letter", containsUppercaseChar],
      ["Contains Lowercase Letter", containsLowercaseChar],
      ["Contains Number", containsNumberChar],
      [
        "Contains Special Character: " + specialChars.join(""),
        containsSpecialChar,
      ],
    ];
  }, []);

  const retypedPasswordSame = (pass, retypedPass) => {
    return pass === retypedPass;
  };

  const boolToClass = (bool) => {
    return bool ? "check-passed" : "check-failed";
  };

  useEffect(() => {
    let allPassed = true;
    requirementTuples.forEach((requirementTuple) => {
      const pass = props.password ? props.password : "";
      if (!requirementTuple[1](pass)) {
        allPassed = false;
        return false;
      }
    });

    if (allPassed) {
      props.setPasswordValid(true);
    } else {
      props.setPasswordValid(false);
    }
  }, [props, requirementTuples]);
  console.log(props.reTypedPassword);

  return (
    <div className={"pass-require"}>
      <ul>
        {requirementTuples.map((requirementTuple) => {
          return (
            <li
              className={boolToClass(requirementTuple[1](props.password))}
              key={requirementTuple[0]}
            >
              {requirementTuple[0]}
            </li>
          );
        })}
        {props.reTypedPassword != null ? (
          <li
            className={boolToClass(
              retypedPasswordSame(props.password, props.reTypedPassword)
            )}
            key={"Passwords are the Same"}
          >
            {"Passwords are the Same"}
          </li>
        ) : null}
      </ul>
    </div>
  );
}

export default PassRequire;
