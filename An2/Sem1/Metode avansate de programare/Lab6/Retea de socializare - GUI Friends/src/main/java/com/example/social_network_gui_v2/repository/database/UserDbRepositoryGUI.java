package com.example.social_network_gui_v2.repository.database;

import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.Validator;
import com.example.social_network_gui_v2.repository.Repository;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

/**
 * DataBase user com.example.social_network_gui_v2.repository made for sql use
 * implements the base interface Repository
 * contains objects of type Long and User
 */
public class UserDbRepositoryGUI implements Repository<Long, UserGUI> {
//    private final String url;
    private final String url;
    private final String username;
    private final String password;
    private final Validator<UserGUI> validator;

    /**
     * Public constructor for the UserDataBase Repository
     * @param url - String
     * @param username - String
     * @param password - String
     * @param validator - Validator
     */
    public UserDbRepositoryGUI(String url, String username, String password, Validator<UserGUI> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }

    @Override
    public UserGUI findOne(Long id) {
        if(id == null)
            throw new IllegalArgumentException("Id must not be null");

        String sql = "SELECT * FROM users where users.id = ?";
        UserGUI user;

        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setInt(1, Math.toIntExact(id));
            ResultSet resultSet = statement.executeQuery();
            if(resultSet.next()){
                String username = resultSet.getString("username");
                String password = resultSet.getString("password");

                user = new UserGUI(username,password);
                user.setId(id);
                return user;
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        return null;
    }

    @Override
    public Iterable<UserGUI> findAll() {
        Set<UserGUI> users = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from users");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String username = resultSet.getString("username");
                String password = resultSet.getString("password");

                UserGUI utilizator = new UserGUI(username,password);
                utilizator.setId(id);
                users.add(utilizator);
            }
            return users;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    @Override
    public UserGUI save(UserGUI entity) {
        if(entity == null)
            throw new IllegalArgumentException("Entity must not be null");
        validator.validate(entity);
        String sql = "insert into users (username,password ) values (?, ?)";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getUsername());
            ps.setString(2, entity.getPassword());

            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public UserGUI delete(Long id) {
        UserGUI user = null;
        String sql = "delete from users where id = ?";

        try(Connection connection = DriverManager.getConnection(url,username,password)) {
            PreparedStatement ps = connection.prepareStatement(sql);
            user = this.findOne(id);
            if(user == null)
                return null;

            ps.setLong(1,id);
            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        return user;
    }

    @Override
    public UserGUI update(UserGUI entity) {
        if(entity == null)
            throw new IllegalArgumentException("Entity must not be null");
        validator.validate(entity);
        String sql = "update users set username = ?, password = ? where id = ?";
        int row_count = 0;

        try(Connection connection = DriverManager.getConnection(url,username,password)) {
            PreparedStatement ps = connection.prepareStatement(sql);

            ps.setString(1,entity.getUsername());
            ps.setString(2,entity.getPassword());
            ps.setLong(3,entity.getId());

            row_count = ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        if(row_count > 0)
            return null;
        return entity;
    }

    @Override
    public UserGUI corespondent(UserGUI friendship) {
        return null;
    }
}
