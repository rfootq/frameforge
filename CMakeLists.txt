set(Namespace_SRCS
        freecad/frameforge/init_gui.py
        freecad/frameforge/__init__.py
        freecad/frameforge/my_numpy_function.py
        freecad/frameforge/translate_utils.py
        freecad/frameforge/version.py
        freecad/frameforge/resources/cool.svg
        freecad/frameforge/resources/translations/frameforge_es-ES.qm
        freecad/frameforge/resources/translations/frameforge_es-ES.ts
)

SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET(SEARCHBAR ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/FrameForge" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBar
)
