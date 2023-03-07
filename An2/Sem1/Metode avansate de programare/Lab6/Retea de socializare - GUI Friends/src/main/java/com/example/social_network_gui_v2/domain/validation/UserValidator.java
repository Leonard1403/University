package com.example.social_network_gui_v2.domain.validation;

import com.example.social_network_gui_v2.domain.UserGUI;

/**
 * User validator where is verified the inputs of an potential user
 */
public class UserValidator implements  Validator<UserGUI>{

    @Override
    public void validate(UserGUI entity) throws ValidationException {
        String first=entity.getUsername();
        String last= entity.getPassword();
        Long id= entity.getId();
//        if(!first.matches("^.[a-z]{0,24}$"))
//            throw new ValidationException("the Username must contain only small letters[25 max], except the first one ");
//        if(!first.matches("^[A-Z].*"))
//            throw new ValidationException("the username must start with a big letter");
    }
}
