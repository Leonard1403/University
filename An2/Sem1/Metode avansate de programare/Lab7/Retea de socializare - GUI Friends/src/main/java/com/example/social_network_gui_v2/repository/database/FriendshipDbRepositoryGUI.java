package com.example.social_network_gui_v2.repository.database;

import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.Tuple;
import com.example.social_network_gui_v2.domain.validation.Validator;
import com.example.social_network_gui_v2.repository.Repository;

import java.sql.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashSet;
import java.util.Set;

/**
 * DataBase friendship com.example.social_network_gui_v2.repository made for sql use
 * implements the base interface Repository
 * contains objects of type Tuple of (Long,Long) and Friendship
 */

public class FriendshipDbRepositoryGUI implements Repository<Tuple<Long,Long>,Friendship> {
    private final String url;
    private final String username;
    private final String password;
//    private final Validator<Friendship> validator;

    /**
     * Public constructor for the FriendshipDataBase Repository
     * @param url - String
     * @param username - String
     * @param password - String
     * @param validator - Validator
     */
    public FriendshipDbRepositoryGUI(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
//        this.validator = validator;
    }

    private Friendship extractFriendship(ResultSet resultSet) throws SQLException{
        Friendship friendship;
        if(resultSet.next()){
            Long id1 = resultSet.getLong("id1");
            Long id2 = resultSet.getLong("id2");
            LocalDateTime date = resultSet.getTimestamp("date").toLocalDateTime();
            String state = resultSet.getString("state");
            String name = resultSet.getString("sendto");

            friendship = new Friendship();
            friendship.setId(new Tuple(id1,id2));
            friendship.setDate(date);
            friendship.setSendTo(name);
            friendship.setState(state);
            return friendship;
        }
        return null;
    }

    @Override
    public Friendship findOne(Tuple<Long, Long> id) {
        if(id == null)
            throw new IllegalArgumentException("Id must not be null");
        Friendship friendship;
        String sql = "SELECT * FROM friendships WHERE id1 = ? AND id2 = ?";
        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement statement = connection.prepareStatement(sql)){

            statement.setInt(1, Math.toIntExact(id.getLeft()));
            statement.setInt(2, Math.toIntExact(id.getRight()));
            ResultSet resultSet = statement.executeQuery();
            friendship = this.extractFriendship(resultSet);
            if(friendship != null)
                return friendship;

            statement.setInt(2, Math.toIntExact(id.getLeft()));
            statement.setInt(1, Math.toIntExact(id.getRight()));
            resultSet = statement.executeQuery();
            friendship = this.extractFriendship(resultSet);
            if(friendship != null)
                return friendship;
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        return null;
    }

    @Override
    public Iterable<Friendship> findAll() {
        Set<Friendship> friendships = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from friendships");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long id1 = resultSet.getLong("id1");
                Long id2 = resultSet.getLong("id2");
                LocalDateTime date = resultSet.getTimestamp("date").toLocalDateTime();
                String state = resultSet.getString("state");
                String name = resultSet.getString("sendto");

                Friendship friendship = new Friendship();
                friendship.setId(new Tuple(id1,id2));
                friendship.setDate(date);
                friendship.setState(state);
                friendship.setSendTo(name);
                friendships.add(friendship);
            }
            return friendships;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return friendships;
    }

    private void executeStatement(Friendship friendship, String sql){
        try(Connection connection = DriverManager.getConnection(url,username,password);
            PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setInt(1, Math.toIntExact(friendship.getId().getLeft()));
            statement.setInt(2, Math.toIntExact(friendship.getId().getRight()));
            statement.executeUpdate();
        }
        catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }

    @Override
    public Friendship corespondent(Friendship friendship){
        if(friendship == null)
            throw new IllegalArgumentException("Entity must not be null");
//        validator.validate(friendship);
        String sql = "update friendships set sendto = ? where id1 = ? and id2 = ?";
//        String sql2 = "update friendships set state = ? where (id2 = ? and id1 = ?)";
        int row_count = 0;

        try(Connection connection = DriverManager.getConnection(url,username,password)) {
            PreparedStatement ps = connection.prepareStatement(sql);
            PreparedStatement ps2 = connection.prepareStatement(sql);

            ps.setString(1,friendship.getSendTo());
            ps.setLong(2,friendship.getId().getLeft());
            ps.setLong(3,friendship.getId().getRight());

//            ps2.setString(1,friendship.getState());
//            ps.setLong(2,friendship.getId2());
//            ps.setLong(3,friendship.getId1());

            row_count = ps.executeUpdate();
//            row_count+= ps2.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        if(row_count > 0)
            return null;
        return friendship;
    }

    @Override
    public Friendship save(Friendship friendship) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyy-MM-dd HH:mm");

        if(friendship == null) {
            throw new IllegalArgumentException("Entity must not be null");
        }
//        validator.validate(friendship);
        String sql = "INSERT INTO Friendships(id1,id2,date,state) VALUES (?,?,'"+friendship.getDate().format(formatter)+"','"+friendship.getState()+"')";
        this.executeStatement(friendship,sql);
        return null;
    }

    @Override
    public Friendship delete(Tuple<Long, Long> id) {
        if(id == null || id.getLeft() == null || id.getRight() == null)
            throw new IllegalArgumentException("Id must not be null");

        Friendship friendship = this.findOne(id);
        if(friendship != null){
            String sql = "DELETE FROM friendships WHERE id1 = ? and id2 = ?";
            this.executeStatement(friendship,sql);
        }
        return friendship;
    }

//    public Friendship changeState(Tuple<Long,Long> id, String state){
//        if(id == null || id.getLeft() == null || id.getRight() == null)
//            throw new IllegalArgumentException("Id must not be null");
//        Friendship friendship = this.findOne(id);
//        if(friendship != null){
//            String sql = "UPDATE friendships SET state = " + state + " WHERE id1 = ? and id2 = ?";
//            this.executeStatement(friendship,sql);
//        }
//    }

    /**
     * Updates the state of a friendship
     */
    @Override
    public Friendship update(Friendship friendship) {

        if(friendship == null)
            throw new IllegalArgumentException("Entity must not be null");
//        validator.validate(friendship);
        String sql = "update friendships set state = ? where id1 = ? and id2 = ?";
//        String sql2 = "update friendships set state = ? where (id2 = ? and id1 = ?)";
        int row_count = 0;

        try(Connection connection = DriverManager.getConnection(url,username,password)) {
            PreparedStatement ps = connection.prepareStatement(sql);
            PreparedStatement ps2 = connection.prepareStatement(sql);

            ps.setString(1,friendship.getState());
            ps.setLong(2,friendship.getId().getLeft());
            ps.setLong(3,friendship.getId().getRight());

//            ps2.setString(1,friendship.getState());
//            ps.setLong(2,friendship.getId2());
//            ps.setLong(3,friendship.getId1());

            row_count = ps.executeUpdate();
//            row_count+= ps2.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        if(row_count > 0)
            return null;
        return friendship;
    }

}
