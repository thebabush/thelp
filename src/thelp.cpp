#include <z3.h>

#include <triton/api.hpp>
#include <triton/pythonBindings.hpp>
#include <triton/pythonObjects.hpp>
#include <triton/tritonToZ3Ast.hpp>

#include <z3++.h>

#include <iostream>


extern "C" {
  Z3_ast convertAstToZ3(PyObject* tritonCtx, Z3_context z3Ctx, PyObject* pyNode) {
    triton::ast::AbstractNode* node = PyAstNode_AsAstNode(pyNode);

    triton::API* api = PyTritonContext_AsTritonContext(tritonCtx);

    triton::ast::TritonToZ3Ast z3Ast{api->getSymbolicEngine(), false};
    triton::ast::AbstractNode* astNode = PyAstNode_AsAstNode(pyNode);
    z3::expr expr = z3Ast.convert(astNode);

    Z3_ast ast = Z3_translate(expr.ctx(), expr, z3Ctx);

    std::cout << "ASD " << node << " " << api << std::endl;

    return ast;
  }
}
