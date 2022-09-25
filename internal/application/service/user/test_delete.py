from internal.application.service.user.test_service_fixtures import TestServiceFixtures


class TestDelete(TestServiceFixtures):
    def test_delete_should_succeed_in_deleting_the_user(self, service, repository, fake):
        id = fake.uuid4()
        deleted_user_counter = 1

        repository.delete.return_value = deleted_user_counter

        returned_deleted_user_counter = service.delete(id=id)

        assert deleted_user_counter == returned_deleted_user_counter

        repository.delete.assert_called_once_with(id=id)

    def test_delete_should_not_succeed_in_deleting_the_user_if_user_id_is_not_found(self, service, repository, fake):
        id = fake.uuid4()
        deleted_user_counter = 0

        repository.delete.return_value = deleted_user_counter

        returned_deleted_user_counter = service.delete(id=id)

        assert deleted_user_counter == returned_deleted_user_counter

        repository.delete.assert_called_once_with(id=id)
