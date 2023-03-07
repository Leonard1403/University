package domain.validation;

import domain.User;

/**
 * User validator where is verified the inputs of an potential user
 */
public class UserValidator implements  Validator<User>{

    @Override
    public void validate(User entity) throws ValidationException {
        String first=entity.getFirstName();
        String last= entity.getLastName();
        Long id= entity.getId();
        if(!first.matches("^.[a-z]{0,24}$"))
            throw new ValidationException("primul nume trebuie sa contina litere mici[25 max], exceptand primul ");
        if(!first.matches("^[A-Z].*"))
            throw new ValidationException("primul nume trb sa inceapa cu litera mare");
        if(!last.matches("^.[a-z]{0,24}$"))
            throw new ValidationException("al 2-lea nume ar trb sa contina litere mici[25 max], exceptand al 2-lea");
        if(!last.matches("^[A-Z].*"))
            throw new ValidationException("ultimul nume ar trb sa inceapa cu litera mare");
    }
}
