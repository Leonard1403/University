package com.example.social_network_gui_v2.repository.database;

import com.example.social_network_gui_v2.domain.Mesaj;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.Validator;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

/**
 * DataBase friendship com.example.social_network_gui_v2.repository made for sql use
 * implements the base interface Repository
 * contains objects of type Tuple of (Long,Long) and Friendship
 */

public class MesajDbRepositoryGUI {
    private final String url;
    private final String username;
    private final String password;

    /**
     * Public constructor for the UserDataBase Repository
     * @param url - String
     * @param username - String
     * @param password - String
     * @param validator - Validator
     */
    public MesajDbRepositoryGUI(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

//    @Override
//    public UserGUI findOne(String nume) {
//        if(nume == null)
//            throw new IllegalArgumentException("Nume must not be null");
//
//        String sql = "SELECT * FROM mesaje where mesaje.nume = ? or mesaje.destinatar = ?";
//        Mesaj msj;
//
//        try(Connection connection = DriverManager.getConnection(url,username,password);
//            PreparedStatement statement = connection.prepareStatement(sql)){
//
//            statement.setString(1, nume);
//
//
//            ResultSet resultSet = statement.executeQuery();
//            if(resultSet.next()){
//                String username = resultSet.getString("username");
//                String password = resultSet.getString("password");
//
//                user = new UserGUI(username,password);
//                user.setId(id);
//                return user;
//            }
//        } catch (SQLException throwables) {
//            throwables.printStackTrace();
//        }
//        return null;
//    }

//    @Override
    public Iterable<Mesaj> findAll(String nume, String destinatar) {
        Set<Mesaj> msj = new HashSet<>();
        System.out.println("Problema");
        System.out.println("Date de intrare: " + nume + " " + destinatar);
        String sql = "SELECT * FROM mesaje WHERE (mesaje.nume = ? AND mesaje.destinatar = ?) OR (mesaje.nume = ? AND mesaje.destinatar = ?) ORDER BY data";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1,nume);
            statement.setString(2,destinatar);
            statement.setString(3,destinatar);
            statement.setString(4,nume);

            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
//                Long id = resultSet.getLong("id");
//                String username = resultSet.getString("username");
//                String password = resultSet.getString("password");

                String nume1, destinatar1, mesaj;
                nume1 = resultSet.getString("nume");
                destinatar1 = resultSet.getString("destinatar");
                mesaj = resultSet.getString("mesaj");

                Mesaj msg = new Mesaj(nume,destinatar,mesaj);

//                UserGUI utilizator = new UserGUI(username,password);
//                utilizator.setId(id);
//                users.add(utilizator);

                msj.add(msg);

            }
            return msj;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println("Problema");
        return msj;
    }

    public Iterable<Mesaj> getAll() {
        Set<Mesaj> msj = new HashSet<>();
//        System.out.println("Problema");
        String sql = "SELECT * FROM mesaje ORDER BY data asc";
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet resultSet = statement.executeQuery()) {

//            statement.setString(1,nume);
//            statement.setString(2,destinatar);

            while (resultSet.next()) {
//                Long id = resultSet.getLong("id");
//                String username = resultSet.getString("username");
//                String password = resultSet.getString("password");

                String nume, destinatar, mesaj;
                nume = resultSet.getString("nume");
                destinatar = resultSet.getString("destinatar");
                mesaj = resultSet.getString("mesaj");

                Mesaj msg = new Mesaj(nume,destinatar,mesaj);

//                UserGUI utilizator = new UserGUI(username,password);
//                utilizator.setId(id);
//                users.add(utilizator);

                msj.add(msg);

            }
            return msj;
        } catch (SQLException e) {
            e.printStackTrace();
        }
//        System.out.println("Problema");
        return msj;
    }
//    @Override
    public Mesaj save(Mesaj entity) {
        if(entity == null)
            throw new IllegalArgumentException("Entity must not be null");
//        validator.validate(entity);
        String sql = "insert into mesaje (nume, destinatar, mesaj, data) values (?, ?, ?, CURRENT_TIMESTAMP)";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getNume());
            ps.setString(2, entity.getDestinatar());
            ps.setString(3, entity.getMesaj());
//            ps.setDate(4, LocalDateTime.now());

            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

//    @Override
//    public UserGUI delete(Long id) {
//        UserGUI user = null;
//        String sql = "delete from users where id = ?";
//
//        try(Connection connection = DriverManager.getConnection(url,username,password)) {
//            PreparedStatement ps = connection.prepareStatement(sql);
//            user = this.findOne(id);
//            if(user == null)
//                return null;
//
//            ps.setLong(1,id);
//            ps.executeUpdate();
//        } catch (SQLException throwables) {
//            throwables.printStackTrace();
//        }
//        return user;
//    }

//    @Override
//    public UserGUI update(UserGUI entity) {
//        if(entity == null)
//            throw new IllegalArgumentException("Entity must not be null");
//        validator.validate(entity);
//        String sql = "update users set username = ?, password = ? where id = ?";
//        int row_count = 0;
//
//        try(Connection connection = DriverManager.getConnection(url,username,password)) {
//            PreparedStatement ps = connection.prepareStatement(sql);
//
//            ps.setString(1,entity.getUsername());
//            ps.setString(2,entity.getPassword());
//            ps.setLong(3,entity.getId());
//
//            row_count = ps.executeUpdate();
//        } catch (SQLException throwables) {
//            throwables.printStackTrace();
//        }
//        if(row_count > 0)
//            return null;
//        return entity;
//    }

//    @Override
    public Mesaj corespondent(Mesaj msj) {
        return null;
    }
}
