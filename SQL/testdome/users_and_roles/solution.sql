CREATE TABLE users_roles (
  userId INTEGER NOT NULL REFERENCES users(id),
  roleId INTEGER NOT NULL REFERENCES roles(id),
  PRIMARY KEY (userId, roleId)
);