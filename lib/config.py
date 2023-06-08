from db.dals import ConfigDAL


async def _create_new_yaml_config(session, **kwargs):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        yaml_config = await yaml_config_dal.create_yaml_config(
            **kwargs
        )
        return yaml_config


async def _create_new_json(hash_yaml, config_json, session):
    async with session.begin():
        yaml_file_dal = ConfigDAL(session)
        yaml_file = await yaml_file_dal.create_json(
            hash_yaml=hash_yaml,
            config_json=config_json,
        )
        return yaml_file


async def _get_yamlconfig_by_hash(hash_yaml, session):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        yaml_config = await yaml_config_dal.get_yamlconfig_by_hashyaml(
            hash_yaml=hash_yaml,
        )
        if yaml_config is not None:
            return yaml_config


async def _get_config_by_hash(hash_yaml, session):
    async with session.begin():
        yaml_file_dal = ConfigDAL(session)
        yaml_file = await yaml_file_dal.get_config_by_hash(
            hash_yaml=hash_yaml,
        )
        if yaml_file is not None:
            return yaml_file


async def _get_config_by_hashyaml(hash_yaml, session):
    async with session.begin():
        yaml_file_dal = ConfigDAL(session)
        yaml_file = await yaml_file_dal.get_yamlconfig_by_hashyaml(
            hash_yaml=hash_yaml,
        )
        if yaml_file is not None:
            return yaml_file


async def _get_yamlconfig_by_nameyaml(name_config, session):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        yaml_config = await yaml_config_dal.get_yamlconfig_by_nameyaml(
            name_config=name_config,
        )
        if yaml_config is not None:
            return yaml_config


async def _get_config_by_config_json(hash_yaml, session):
    async with session.begin():
        yaml_file_dal = ConfigDAL(session)
        yaml_file = await yaml_file_dal.get_config_by_config_json(
            hash_yaml=hash_yaml,
        )
        if yaml_file is not None:
            return yaml_file


async def _delete_yaml_config(name_config, session):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        deleted_config = await yaml_config_dal.delete_yaml_config(
            name_config=name_config,
        )
        return deleted_config


async def _update_yaml_config(name_config, session):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        updated_yaml_config = await yaml_config_dal.update_yaml_config(
            name_config=name_config
        )
        return updated_yaml_config


async def _update_config(hash_yaml, name_esphome, platform, session):
    async with session.begin():
        yaml_config_dal = ConfigDAL(session)
        updated_yaml_config = await yaml_config_dal.update_config(
            hash_yaml=hash_yaml,
            name_esphome=name_esphome,
            platform=platform
        )
        return updated_yaml_config


async def _update_config_json(hash_yaml, config_json, session):
    async with session.begin():
        config_dal = ConfigDAL(session)
        update_config = await config_dal.update_config_json(
            hash_yaml=hash_yaml, config_json=config_json
        )
        return update_config
