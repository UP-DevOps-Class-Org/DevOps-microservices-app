package com.example.AuthenticationApp.repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;
import com.example.AuthenticationApp.model.ERole;
import com.example.AuthenticationApp.model.Role;


@Repository
public interface RoleRepository extends JpaRepository<Role, Long> {

    Optional<Role> findByName(ERole roleName); 
}
