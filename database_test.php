<?php 
    $user = 'root';
    $pass = 'root';
    $db = 'inventory';
    $host = 'localhost';

    $conn = new PDO(
        "mysql:host=$host;dbname=$db",
        $user,
        $pass
    );

    $stmt = $conn->prepare(
        "INSERT INTO user 
        (nama_user, role) 
        values ('Admin', 'admin')"
    );
    $stmt->execute();
    
?>